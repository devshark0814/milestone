<template>
  <v-card>
    <v-card-title class="bg-primary">プロジェクト情報</v-card-title>

    <v-card-text>
      <v-container class="pt-8">
        <v-form>
          <v-row>
            <v-col>
              <v-text-field v-model="sPjModel.title" label="プロジェクト名" outlined clearable hide-details="auto"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <MonthPicker v-model="sPjModel.start" label="開始日" />
            </v-col>
            <v-col>
              <MonthPicker v-model="sPjModel.end" label="終了日" />
            </v-col>
            <v-col>
              <v-text-field v-model="sPjModel.progress" label="進捗率" outlined clearable hide-details="auto" type="number" />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-color-picker
                v-model="sPjModel.color"
                hide-inputs
                hide-mode-switch
                hide-sliders
              ></v-color-picker>
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
export default {

  components: {
    MonthPicker,
  },

  data() {
    return {
      sPjModel: {}
    };
  },

  computed: {
    ...mapGetters('gantt', ['getPjModel']),
  },

  mounted() {
    this.sPjModel = {...this.getPjModel};
  },

  methods: {
    ...mapActions('gantt',['changePjModel']),

    close() {
      this.$emit('close');
    },

    save() {
      // TODO 登録
      console.log(this.sPjModel)
      this.changePjModel(this.sPjModel);
      this.$emit('close');
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