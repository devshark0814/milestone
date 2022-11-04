const state = {
  user: {}
};

const getters = {
  getUser(state) {
    return state.user;
  }
};

const actions = {
  changeUser({ commit }, val) {
    commit("changeUser", val);
  }
};

const mutations = {
  changeUser(state, value) {
    state.user = value;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};