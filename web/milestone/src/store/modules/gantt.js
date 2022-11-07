const state = {
  ganttType: 'months',
  pjModel: {}
};

const getters = {
  getGanttType(state) {
    return state.ganttType;
  },
  getMilestoneModel(state) {
    return state.pjModel;
  },
};

const actions = {
  changeGanttType({ commit }, val) {
    commit("changeGanttType", val);
  },
  changeMilestoneModel({ commit }, val) {
    commit("changeMilestoneModel", val);
  },
};

const mutations = {
  changeGanttType(state, value) {
    state.ganttType = value;
  },
  changeMilestoneModel(state, value) {
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