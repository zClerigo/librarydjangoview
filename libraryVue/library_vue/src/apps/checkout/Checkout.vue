<template>
    <div>
        <p>
        Hello vue from checkout {{  bookList }}
        </p>
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
        With fetch this time
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
            this.bookList = ext_book_list,
            this.selectedBooks = this.bookList.filter((book) => book.checkedOut)

            console.log(this.csrf_token)
        },
        methods: {
        },
        computed: {
            submit_form_fetch(){
                console.log("fetching")
                this.form_error = []
                this.form_updated = ""
                let formData = new FormData();
                let form_data = {
                        'selectedBooks': this.selectedBooks
                }
                for (var key in form_data) {
            		formData.append(key, form_data[key])
        	    }
                fetch(this.update_bis_url,
            	{
                	method: "post",
                	body: formData,
                	headers: {'X-CSRFToken': this.csrf_token},
                	credentials: 'same-origin'
            	}
        	).then(function(response) {
            	console.log('response', response)
            	return response.json()}).then(
	            	this.handleResponse).catch(
	                	(error) => {
	                	console.log('error', String(error))
	                	this.form_error=["error"]
    			})
            console.log(formData)
            },
            handleResponse(response) {
                console.log('json response', response)
                if ('success' in response){
                        if (response['success'] == true) {
                            this.form_updated = "Movie has been updated"
                        } else {
                            if ('errors' in response){
                                    for (const [key, value] of Object.entries(response['errors'])) {
                                        for (const error of value) {
                                                this.form_error.push(`${key}: ${error}`)
                                        }
                                    }
                            } else {
                                    this.form_error=["Update failed - An error occurred but do not have more information about it"]
                            }
                        }
                } else {
                            this.form_error=["Update failed - It has been an error on the form request"]
                }
            }
        }
    }
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>