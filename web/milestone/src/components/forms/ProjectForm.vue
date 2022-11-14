<template>
  <v-card>
    <v-card-title class="bg-primary">プロジェクト情報</v-card-title>

    <v-card-text>
      <v-container class="pt-8">
        <v-form>
          <v-row>
            <v-col>
              <v-text-field v-model="projectModel.name" label="プロジェクト名" outlined clearable hide-details="auto"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-textarea v-model="projectModel.description" label="プロジェクト説明" outlined clearable hide-details="auto"></v-textarea>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-autocomplete
                v-model="projectModel.priority"
                label="優先度"
                :items="priorityList"
                item-text="text"
                item-value="value"
                outlined clearable hide-details="auto">
              </v-autocomplete>
            </v-col>
            <v-col>
              <v-text-field v-model="projectModel.sale_cost" label="見積工数" outlined clearable hide-details="auto"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <MonthPicker v-model="projectModel.planned_release_date" label="リリース予定日" />
            </v-col>
            <v-col>
              <MonthPicker v-model="projectModel.fact_release_date" label="リリース日" />
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="close">Close</v-btn>
      <v-btn color="blue darken-1" text @click="save">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import { mapGetters } from 'vuex'
import MonthPicker from '@/components/MonthPicker'
export default {

  components: {
    MonthPicker,
  },

  data() {
    return {
      name: '',
      priorityList: [
        { text: '低め', value: 1 },
        { text: '可能なら', value: 2 },
        { text: '通常', value: 3 },
        { text: '高め', value: 4 },
        { text: '緊急', value: 5 }
      ],

      projectModel: {}
    };
  },

  computed: {
    ...mapGetters('project', ['getProjectModel']),
  },

  mounted() {
    this.projectModel = {...this.getProjectModel};
  },

  methods: {
    close() {
      this.$emit('close');
    },

    save: async function() {
      const method = ('id' in this.projectModel) ? 'PUT' : 'POST'
      const url = ('id' in this.projectModel) ? 'projects/' + this.projectModel.id : 'projects/'
      await this.$axios({
        method: method,
        url: url,
        data: this.projectModel
      })
      .then(res => {
        alert('処理完了')
        this.close()
      })
    }
  }
};
</script>
<style>
.bg-primary {
  background-color: var(--v-primary-base) !important;
  color: white !important;
}
</style>