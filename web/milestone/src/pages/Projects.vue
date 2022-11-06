<template>
  <div>
    <v-card flat class="pa-3">
      <v-data-table
        :headers="headers"
        :items="desserts"
        :search="searchText"
        class="elevation-0 pa-3"
        @click:row="clickRow"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-text-field
              v-model="searchText"
              outlined
              placeholder="Search User"
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
      </v-data-table>
    </v-card>
    <!-- <UserDialog :dialog="userDialog" @close="userDialog=false"/> -->
  </div>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        { text: 'id', value: 'id' },
        { text: 'プロジェクト名', value: 'name' },
        { text: '説明', value: 'description' },
        { text: '見積工数', value: 'sale_cost' },
        { text: 'リリース予定日', value: 'planned_release_date' },
        { text: 'リリース日', value: 'fact_release_date' },
      ],
      desserts: [
        { id: 1, name: 'AAA', description: '', sale_cost: 199, planned_release_date: '2022-10-01', fact_release_date: '2022-11-01' },
      ],
      searchText: '',
    }
  },

  methods: {
    clickRow(item) {

    },

    clickNew() {

    }
  }
}
</script>