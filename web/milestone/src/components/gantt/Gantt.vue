<template>
  <DxGantt
    :task-list-width="500"
    :height="700"
    :scale-type="getGanttType"
    @task-edit-dialog-showing="onTaskEditDialogShowing"
    :task-content-template="taskContentTemplate"
    @task-click="onTaskClick"
    :ref="ganttRef"
    @content-ready="onContentReady"
  >

    <DxTasks :data-source="milestones" assign-user-ids-expr="assign_user_ids"/>
    <!-- <DxDependencies :data-source="dependencies"/>
    <DxResources :data-source="resources"/>
    <DxResourceAssignments :data-source="resourceAssignments"/> -->

    <!-- <DxToolbar>
      <DxItem name="undo"/>
      <DxItem name="redo"/>
      <DxItem name="separator"/>
      <DxItem name="collapseAll"/>
      <DxItem name="expandAll"/>
      <DxItem name="separator"/>
      <DxItem name="addTask"/>
      <DxItem name="deleteTask"/>
      <DxItem name="separator"/>
      <DxItem name="zoomIn"/>
      <DxItem name="zoomOut"/>
    </DxToolbar> -->

    <DxEditing :enabled="true" :allow-task-updating="true" />
    <DxContextMenu :enabled="false" />
    <!-- <DxValidation :auto-update-parent-tasks="true"/> -->

    <DxColumn
      :width="200"
      data-field="title"
      caption="プロジェクト"
    />
    <DxColumn
      :width="100"
      data-field="start"
      caption="開始日"
      data-type="date"
    />
    <DxColumn
      :width="100"
      data-field="end"
      caption="終了日"
      data-type="date"
    />
    <DxColumn
      :width="1"
      data-field="assign_user_ids"
      caption="アサイン"
      data-type="string"
    />
    <template #taskContentTemplate="{ data: item }">
      <div
        class="custom-row"
        :style="{width: item.taskSize.width + 'px', backgroundColor: item.taskData.color }"
      >
        <div class="custom-task-wrapper">
          <div class="custom-task-title">{{ item.taskData.title }}</div>
        </div>
        <div
          class="custom-task-progress"
          :style="{width: item.taskData.progress + '%'}"
        />
        <div style="position: absolute;">
          <template v-for="(user,i) in user_ids(item.taskData.assign_user_ids)">
            <v-avatar
              :key="i"
              color="primary"
              size="40"
              class="mr-2 mt-1"
            >
              <span class="white--text text-h5">{{ userName(user) }}</span>
            </v-avatar>
          </template>
        </div>
      </div>
    </template>
    <ComDialog :dialog="comDialog" form="MilestoneForm" @close="closeDialog"/>
  </DxGantt>
</template>
<script>
import {
  DxGantt,
  DxTasks,
  // DxDependencies,
  // DxResources,
  // DxResourceAssignments,
  DxColumn,
  DxEditing,
  DxValidation,
  DxToolbar,
  DxItem,
  DxContextMenu,
} from 'devextreme-vue/gantt';
import { locale } from 'devextreme/localization';


import { mapGetters, mapActions } from 'vuex';
import ComDialog from '@/components/ComDialog.vue';
const ganttRef = 'gantt';
export default {
  components: {
    DxGantt,
    DxTasks,
    // DxDependencies,
    // DxResources,
    // DxResourceAssignments,
    DxColumn,
    DxEditing,
    DxValidation,
    DxToolbar,
    DxItem,
    DxContextMenu,
    ComDialog
  },

  data() {
    return {
      ganttRef,
      milestones: [],
      comDialog: false,
      taskContentTemplate: '',
      // dependencies,
      // resources,
      // resourceAssignments,
      userList:[
        { text: '下津曲', value: 1 , img: ''},
        { text: '山口', value: 2 , img: ''},
        { text: '垂野', value: 3 , img: ''},
      ],
    };
  },

  created() {
    locale('jp');
    this.search()
  },

  computed: {
    ...mapGetters('gantt', ['getGanttType']),

    gantt: function() {
      return this.$refs[ganttRef].instance;
    },

    user_ids: function(v) {
      return function(v){
        return v.split(',').map(Number);
      }
    },

    userName: function(v) {
      return function(v) {
        let item = this.userList.find((item) => item.value === v);
        return item.text.substr(0, 1)
      }
    }
  },

  watch: {
    /** 期間切り替え時に再描画 */
    getGanttType: function(newv, oldv) {
      this.gantt.refresh();
    }
  },

  methods: {
    ...mapActions('gantt', ['changeMilestoneModel']),

    search() {
      this.$axios
        .get("milestones/")
        .then(res => {
          this.milestones = res.data
          this.gantt.refresh();
        })
    },

    /** デフォルトの編集モーダルは非表示 */
    onTaskEditDialogShowing(obj) {
      obj.cancel = true;
    },

    /** PJクリック時に編集モーダルを表示する */
    onTaskClick(obj) {
      let id = obj.data.id
      let milestone = this.milestones.find((v) => v.id == id)
      // store
      this.changeMilestoneModel(milestone);
      // dialog open
      this.comDialog = true;
    },

    closeDialog(){
      this.comDialog = false
      this.search()
    },

    /** ガント線のTop属性を変更 */
    styleOverwrite() {
      const elm = document.getElementsByClassName('dx-gantt-taskWrapper');
      for (let i = 0; i < elm.length; i++) {
        let top = Number(elm[i].style.top.replace('px', ''))
        elm[i].style.top = String(top - 20) + 'px'
      }
    },

    // ガントがReady状態になった場合
    onContentReady() {
      // ガント線のTop属性を変更
      this.styleOverwrite()
    }
  },
};
</script>
<style>
  #gantt {
    height: 700px;
  }

.dx-treelist-headers.dx-treelist-nowrap {
  background-color: var(--v-primary-base) !important;
  color: white !important;
}

.dx-gantt-tsac{
  color: white !important;
}
.dx-gantt-tsac > .dx-gantt-tsa {
  background-color: var(--v-primary-base) !important;
}

/* 左側のエリアの行高さ-------------- */
.dx-gantt .dx-row {
  height: 100px;
}
/* --------------------------------- */

/* 右側のエリアの行高さ-------------- */
.custom-row {
  /* background-color: red; */
  max-height: 100px;
  height: 100%;
  display: block;
  overflow: hidden;
}
.custom-task-wrapper {
  padding: 8px;
  color: #fff;
}
.custom-task-wrapper > * {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
}
.custom-task-title {
  font-weight: 600;
  font-size: 13px;
}
.custom-task-progress {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 0%;
  height: 8px;
  background: rgba(0, 0, 0, 0.3);
}
/* --------------------------------- */
</style>
