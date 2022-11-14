<template>
  <div>
    <v-card flat class="pa-3">
      <v-data-table
        :headers="headers"
        :items="desserts"
        :search="searchText"
        class="elevation-0 pa-3"
        :fixed-header="true"
        :footer-props="{
          'items-per-page-options': [50, 100, 150, -1],
          showFirstLastPage: true
        }"
        @click:row="clickRow"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-text-field
              v-model="searchText"
              outlined
              placeholder="Search"
              hide-details
              dense
            >
            </v-text-field>
            <v-spacer></v-spacer>
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
        </template>
        <template v-slot:item.priority="{item}">
          <PriorityChip :priority="item.priority" />
        </template>
      </v-data-table>
    </v-card>
    <ComDialog :dialog="comDialog" form="ProjectForm" @close="dialogClose"/>
  </div>
</template>
<script>
import ComDialog from '@/components/ComDialog.vue';
import PriorityChip from '@/components/PriorityChip.vue';
import { mapActions } from 'vuex'
export default {

  components: {
    ComDialog,
    PriorityChip
  },

  data() {
    return {
      headers: [
        { text: 'id', value: 'id' },
        { text: 'プロジェクト名', value: 'name' },
        { text: '説明', value: 'description' },
        { text: '優先度', value: 'priority' },
        { text: '見積工数', value: 'sale_cost' },
        { text: 'リリース予定日', value: 'planned_release_date' },
        { text: 'リリース日', value: 'fact_release_date' },
      ],
      desserts: [],
      searchText: '',
      comDialog: false,
    }
  },

  created() {
    this.search()
  },

  methods: {
    ...mapActions('project', ['changeProjectModel']),
    search() {
      this.$axios
        .get("projects/")
        .then(res => {
          this.desserts = res.data
        })
    },

    clickRow(item) {
      this.changeProjectModel(item)
      this.comDialog = true;
    },

    clickNew() {
      this.changeProjectModel({})
      this.comDialog = true;
    },

    dialogClose() {
      this.comDialog=false
      this.search()
    }
  }
}
</script>