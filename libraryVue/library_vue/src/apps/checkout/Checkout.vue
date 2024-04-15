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
        mounted() {
            this.csrf_token = ext_csrf_token,
            this.form = ext_form
        },
        data: function() {
            return {
                csrf_token: window.ext_csrf_token,
                form: window.ext_form,
            }
        },
        methods: {
        },
    }
</script>