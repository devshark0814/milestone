<template>
  <v-card>
    <v-card-title class="bg-primary">マイルストーン情報</v-card-title>

    <v-card-text>
      <v-container class="pt-8">
        <v-form>
          <v-row>
            <v-col>
              優先度:<PriorityChip :priority="model.project_priority" class="ml-5"/>
            </v-col>
            <v-spacer />
            <v-col class="text-right">
              <v-swatches
                v-model="color"
                popover-x="left"
                popover-y="bottom"
                swatches="text-advanced"
              ></v-swatches>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-autocomplete
                v-if="!model.id"
                v-model="model.title"
                label="プロジェクト名"
                :items="projectList"
                item-text="text"
                item-value="value"
                @change="changeProject"
                outlined clearable hide-details="auto">
              </v-autocomplete>
              <v-text-field v-else v-model="model.title" label="プロジェクト名" outlined readonly></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <MonthPicker v-model="model.start" label="開始日" />
            </v-col>
            <v-col>
              <MonthPicker v-model="model.end" label="終了日" />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-autocomplete
                v-model="users"
                label="アサイン"
                :items="userList"
                item-text="text"
                item-value="value"
                multiple
                outlined clearable hide-details="auto">
              </v-autocomplete>
            </v-col>
            <v-col>
              <v-text-field v-model.number="model.progress" type="number" label="進捗率" outlined clearable hide-details="auto"></v-text-field>
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
import { mapGetters, mapActions } from 'vuex'
import MonthPicker from '@/components/MonthPicker'
import PriorityChip from '@/components/PriorityChip.vue';
import VSwatches from 'vue-swatches'
import "vue-swatches/dist/vue-swatches.css"
export default {

  components: {
    MonthPicker,
    PriorityChip,
    VSwatches
  },

  data() {
    return {
      model: {},
      userList:[
        { text: '下津曲', value: 1 , img: ''},
        { text: '山口', value: 2 , img: ''},
        { text: '垂野', value: 3 , img: ''},
      ],
      users: [],
      color: '#000000',

      projects: [],
      projectList: [],
    };
  },

  computed: {
    ...mapGetters('gantt', ['getMilestoneModel']),
  },

  watch: {
    // ドラッグして日付を変更されるとフォーマットが崩れるので再フォーマット
    'model.start': function(newVal, oldVal) {
      this.model.start = new Date(newVal).toISOString().substr(0, 10)
    },
    'model.end': function(newVal, oldVal) {
      this.model.end = new Date(newVal).toISOString().substr(0, 10)
    }
  },

  mounted() {
    this.model = {...this.getMilestoneModel};
    if (!Object.keys(this.model).length) {
      this.search()
      return;
    }
    this.users = this.model.assign_user_ids.split(',').map(Number);
    this.color = this.model.color;
  },

  methods: {
    ...mapActions('gantt',['changeMilestoneModel']),

    search:async function() {
      await this.$axios
        .get("projects/")
        .then(res => {
          this.projects = res.data
          this.projectList = this.projects.map((v) => ({
            text: v.name,
            value: v.id
          }))
        })
    },

    close() {
      this.$emit('close');
    },

    save: async function() {
      // TODO ドラッグで期間を編集した際のsave
      const method = ('id' in this.model) ? 'PUT' : 'POST'
      const url = ('id' in this.model) ? 'milestones/' + this.model.id : 'milestones/'
      this.model.color = this.color;
      this.model.assign_user_ids = this.users.join(',');
      await this.$axios({
        method: method,
        url: url,
        data: this.model
      })
      .then(res => {
        alert('処理完了')
        this.close()
      })
    },

    /** プロジェクト変更時（新規時のみ） */
    changeProject(id) {
      this.model = {
        project_id: id,
        assign_user_ids: '',
        start_date: '',
        end_date: '',
        progress: '',
        color: ''
      }
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