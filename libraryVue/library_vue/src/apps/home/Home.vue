<template>
    <h1>Welcome back! Here are the books you have checked out so far</h1><br/>
    <ul>
        <li v-for="book in bookList">
            <h3>{{ book.name }}</h3>
            <p>author: {{ book.author }}</p>
            <p>checkout date: {{ book.checkout_date }}</p>
        </li>
    </ul>
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
                bookList: ''
            }
        },
        mounted() {
            this.csrf_token = ext_csrf_token,
            this.bookList = ext_checkedbooks,

            console.log(this.csrf_token)
        },
        methods: {
        },
    }
</script>