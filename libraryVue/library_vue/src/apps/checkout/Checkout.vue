<template>
    <div>
        <h1>Select a book to check it out and deselect a book to return it</h1>
        <form method="post" class="form">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
        <multiselect v-model="selectedBooks" :options="bookList" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="select a book" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
            <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
        </multiselect>
        <button type="submit" class="btn btn-primary"
            @click.prevent="submit_form_fetch"
            :disabled="submitting_form">
            Submit
        </button>
        <br><br>
        <div v-if="form_error">
            <ul>
                <li v-for="(error, index) in form_error">
                    {{error}}
                </li>
            </ul>
        </div>
        <div v-if="form_updated">
            {{ form_updated }}
        </div>
    </form>
    </div>
</template>
<script>
    import VueDatePicker from '@vuepic/vue-datepicker';
    import '@vuepic/vue-datepicker/dist/main.css'
    import Multiselect from 'vue-multiselect'

    export default {
        name: 'App',
        components: {
            VueDatePicker,
            Multiselect
        },
        data: function() {
            return {
                csrf_token: '',
                form: '',
                selectedBooks: [],
                bookList: [],
                update_bis_url: ext_update_bis_url,
                submitting_form: false,
                form_error: [],
                form_updated: ""
            }
        },
        mounted() {
            this.csrf_token = ext_csrf_token,
            this.bookList = ext_book_list.map(item => ({
                name: item.fields.name, 
                id: item.pk,
                checkedOut: item.fields.checked_out
            }));
            console.log(this.bookList)
            this.selectedBooks = this.bookList.filter((book) => book.checkedOut)
        },
        // methods: {
        // },
        methods: {
            submit_form_fetch() {
                console.log("fetching")
                this.form_error = []
                this.form_updated = ""
                let formData = new FormData();
                let indexes = this.selectedBooks.map(obj => obj.id)
                console.log("selected", indexes)

                indexes.forEach(id => {
                    formData.append('selectedBooks[]', id);
                });

                fetch(this.update_bis_url, {
                    method: "POST",
                    body: formData,
                    headers: {'X-CSRFToken': this.csrf_token},
                    credentials: 'same-origin'
                }).then(function(response) {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                }).then(this.handleResponse).catch((error) => {
                    console.error('Error during fetch:', error);
                    this.form_error = ["An unexpected error occurred. Please try again later."];
                });
            },
            handleResponse(response) {
                console.log('json response', response);
                if (response['success'] === true) {
                    this.form_updated = "Movie has been updated";
                } else {
                    if ('errors' in response) {
                        for (const [key, value] of Object.entries(response['errors'])) {
                            for (const error of value) {
                                this.form_error.push(`${key}: ${error}`);
                            }
                        }
                    } else {
                        this.form_error = ["Update failed - An error occurred but do not have more information about it"];
                    }
                }
            }
        }
    }
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>