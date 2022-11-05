import Vue from "vue";
import Vuex from "vuex";

import user from "./modules/user";
import gantt from "./modules/gantt";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    user,
    gantt
  }
});

export default store;