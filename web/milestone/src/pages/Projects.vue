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
          <v-chip
            label
            :color="priorityColor(item.priority)"
            :text-color="priorityTextColor(item.priority)"
          >
            {{ priorityName(item.priority) }}
          </v-chip>
        </template>
      </v-data-table>
    </v-card>
    <ComDialog :dialog="comDialog" form="ProjectForm" @close="dialogClose"/>
  </div>
</template>
<script>
import ComDialog from '@/components/ComDialog.vue';
import { mapActions } from 'vuex'
export default {

  components: {
    ComDialog,
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

  computed: {
    priorityName: (v) => {
      return (v) => {
        console.log(v)
        switch (v) {
          case 1:
            return '低め'
          case 2:
            return '可能なら'
          case 3:
            return '通常'
          case 4:
            return '高め'
          default:
            return '緊急'
        }
      }
    },
    priorityColor: (v) => {
      return (v) => {
        if(v==4) return 'orange lighten'
        if(v==5) return 'red darken-1'
        return 'light-blue lighten-5'
      }
    },
    priorityTextColor: (v) => {
      return (v) => {
        if(v==4 || v==5) return 'white'
        return 'light-blue darken-1'
      }
    },
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