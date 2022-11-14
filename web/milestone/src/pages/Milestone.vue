<template>
  <div>
    <v-toolbar flat color="orange accent-1" :height="100">
      <v-autocomplete
        v-model="type"
        label="表示期間設定"
        placeholder="表示期間を選択してください"
        :items="types"
        background-color="white"
        hide-details
        hide-selected
        outlined
        flat
        class="pa-2"
        item-key="text"
        item-value="id"
        @change="changeType"
      >
      </v-autocomplete>
      <v-spacer />
      <v-btn
            depressed
            color="primary"
            class="mt-1"
            @click="clickNew"
      >
        <v-icon class="mr-2">mdi-account-multiple-plus</v-icon>
          新規追加
      </v-btn>
    </v-toolbar>
    <v-row class="pt-5">
      <v-col>
        <Gantt />
      </v-col>
    </v-row>
    <ComDialog :dialog="comDialog" form="MilestoneForm" @close="dialogClose"/>
  </div>
</template>
<script>
import { mapActions } from 'vuex'
import Gantt from '@/components/gantt/Gantt.vue';
import ComDialog from '@/components/ComDialog.vue';
export default {

  components: {
    Gantt,
    ComDialog
  },

  data() {
    return {
      type: 'months',
      comDialog: false,
      types: [
        { text: '月表示', id: 'months' },
        { text: '四半期表示', id: 'quarters' },
        { text: '年表示', id: 'years' },
      ]
    };
  },

  methods: {
    ...mapActions('gantt',['changeGanttType', 'changeMilestoneModel']),

    /** タイプの更新 */
    changeType() {
      this.changeGanttType(this.type);
    },

    clickNew() {
      this.changeMilestoneModel({});
      this.comDialog = true;
    },

    dialogClose() {
      this.comDialog = false;
    }
  },
};
</script>
