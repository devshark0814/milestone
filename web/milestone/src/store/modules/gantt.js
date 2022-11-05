const state = {
  ganttType: 'months'
};

const getters = {
  getGanttType(state) {
    return state.ganttType;
  }
};

const actions = {
  changeGanttType({ commit }, val) {
    commit("changeGanttType", val);
  }
};

const mutations = {
  changeGanttType(state, value) {
    state.ganttType = value;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};