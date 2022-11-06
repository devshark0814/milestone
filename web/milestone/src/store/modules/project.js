const state = {
  projectModel: {}
};

const getters = {
  getProjectModel(state) {
    return state.projectModel;
  },
};

const actions = {
  changeProjectModel({ commit }, val) {
    commit("changeProjectModel", val);
  },
};

const mutations = {
  changeProjectModel(state, value) {
    state.projectModel = value;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};