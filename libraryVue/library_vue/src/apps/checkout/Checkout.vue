<template>
    <div>
        <p>
        Hello vue from checkout {{  csrf_token }}
        </p>
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
                bookList: []
            }
        },
        mounted() {
            this.csrf_token = ext_csrf_token,
            this.form = ext_form,

            console.log(this.csrf_token)
        },
        methods: {
        },
    }
</script>