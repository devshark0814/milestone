import Vue from "vue";
import Vuex from "vuex";

import user from "./modules/user";
import gantt from "./modules/gantt";
import project from "./modules/project";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    user,
    gantt,
    project
  }
});

export default store;