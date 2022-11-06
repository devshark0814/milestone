<template>
  <v-card>
    <v-card-title class="bg-primary">ユーザー登録</v-card-title>

    <v-card-text>
      <v-container class="pt-8">
        <v-form>
          <v-row>
            <v-col>
              <v-text-field v-model="user.name" label="氏名" outlined clearable hide-details="auto"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field v-model="user.image" label="画像" outlined clearable hide-details="auto"></v-text-field>
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
export default {
  data() {
    return {
      user: {}
    };
  },

  computed: {
    ...mapGetters('user', ['getUser']),
  },

  mounted() {
    this.user = {...this.getUser};
  },

  methods: {
    close() {
      this.$emit('close');
    },

    save() {
      this.close()
      this.$axios
        .post("users/",this.user)
        .then(res => {
          console.info(res);
          alert('登録しました')
        })
        .catch(err => {
          alert('失敗しました')
          console.err(err);
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