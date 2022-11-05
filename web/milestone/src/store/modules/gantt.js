const state = {
  ganttType: 'months',
  pjModel: {}
};

const getters = {
  getGanttType(state) {
    return state.ganttType;
  },
  getPjModel(state) {
    return state.pjModel;
  },
};

const actions = {
  changeGanttType({ commit }, val) {
    commit("changeGanttType", val);
  },
  changePjModel({ commit }, val) {
    commit("changePjModel", val);
  },
};

const mutations = {
  changeGanttType(state, value) {
    state.ganttType = value;
  },
  changePjModel(state, value) {
    state.pjModel = value;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};