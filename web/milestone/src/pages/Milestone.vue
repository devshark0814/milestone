<template>
  <div>
    <!-- <v-row>
      <v-col>
        <
      </v-col>
    </v-row> -->
    <v-toolbar flat color="orange accent-1" :height="100">
      <v-autocomplete
        v-model="type"
        label="表示期間設定"
        placeholder="表示期間を選択してください"
        :items="['months', 'quarters', 'years']"
        background-color="white"
        hide-details
        hide-selected
        outlined
        flat
        class="pa-2"
        @change="changeType"
      >
      </v-autocomplete>
    </v-toolbar>
    <v-row class="pt-5">
      <v-col>
        <Gantt />
      </v-col>
    </v-row>
  </div>
</template>
<script>
import { mapActions } from 'vuex'
import Gantt from '@/components/gantt/Gantt.vue';
export default {

  components: {
    Gantt
  },

  data() {
    return {
      type: 'months',
    };
  },

  methods: {
    ...mapActions('gantt',['changeGanttType']),

    /** タイプの更新 */
    changeType() {
      this.changeGanttType(this.type);
    }
  },
};
</script>
