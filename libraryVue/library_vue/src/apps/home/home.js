import 'vite/modulepreload-polyfill';

import { createApp } from 'vue';
import App from './Home.vue'

createApp(App).mount("#app")