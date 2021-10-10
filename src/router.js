import { createWebHistory, createRouter } from "vue-router";

let routes = [{
        path: "/",
        alias: "/esdls",
        name: "esdls",
        component: () =>
            import ("./components/TutorialsList"),
    },
    {
        path: "/esdls/:id",
        name: "tutorial-details",
        component: () =>
            import ("./components/Tutorials"),
    },
    {
        path: "/add",
        name: "add",
        component: () =>
            import ("../src/components/AddTutorial.vue"),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;