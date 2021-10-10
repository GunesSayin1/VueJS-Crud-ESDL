import { createApp } from "vue";
import App from "./App.vue";
import {
    Card,
    Button,
    Menu,
    Form,
    Input,
    Row,
    Col,
    Switch,
    Table,
    Tag,
    Checkbox,
    message,
    Upload,
} from "ant-design-vue";
import router from "./router";

import "ant-design-vue/dist/antd.css";

createApp(App)
    .use(Card)
    .use(message)
    .use(Checkbox)
    .use(Button)
    .use(router)
    .use(Row)
    .use(Col)
    .use(Upload)
    .use(Table)
    .use(Switch)
    .use(Form)
    .use(Tag)
    .use(Input)
    .use(Menu)
    .mount("#app");