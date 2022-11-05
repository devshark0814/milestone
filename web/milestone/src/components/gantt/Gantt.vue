<template>
  <DxGantt
    :task-list-width="500"
    :height="700"
    :scale-type="getGanttType"
    @task-edit-dialog-showing="onTaskEditDialogShowing"
    :task-content-template="taskContentTemplate"
  >

    <DxTasks :data-source="tasks" />
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
      :width="300"
      data-field="title"
      caption="プロジェクト"
    />
    <DxColumn
      data-field="start"
      caption="開始日"
      data-type="date"
    />
    <DxColumn
      data-field="end"
      caption="終了日"
      data-type="date"
    />
    <template #taskContentTemplate="{ data: item }">
      <div
        class="custom-row"
        :style="{width: item.taskSize.width + 'px', backgroundColor: item.taskData.color }"
      >
        <div class="custom-task-wrapper">
          <div class="custom-task-title">{{ item.taskData.title }}</div>
        </div>
      </div>
    </template>
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


import { mapGetters } from 'vuex';

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
    DxContextMenu
  },
  data() {
    return {
      tasks: [
        {
          id: 1,
          parentId: 0,
          title: 'LP構成簡単くん',
          start: new Date('2022-11-01'),
          end: new Date('2023-01-15'),
          progress: 0,
          color: 'red'
        },
        {
          id: 2,
          parentId: 0,
          title: 'モンKEY',
          start: new Date('2022-11-01'),
          end: new Date('2023-01-15'),
          progress: 0,
          color: 'blue'
        }
      ],
      // dependencies,
      // resources,
      // resourceAssignments,
    };
  },

  created() {
    locale('jp');
  },

  computed: {
    ...mapGetters('gantt', ['getGanttType']),
  },

  methods: {
    onTaskEditDialogShowing(obj) {
      // if() {

      // }
      console.log(obj)
      obj.cancel = true;
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
  height: 63px;
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
/* --------------------------------- */
</style>
