<template>
  <div>
    <v-card flat class="pa-3">
      <v-data-table
        :headers="headers"
        :items="desserts"
        class="elevation-0 pa-3"
        @click:row="clickRow"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-text-field
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
        <template v-slot:item.name="{ item }">
          <v-avatar size="48" color="teal" class="ma-2">
            <img src="../assets/user.jpg" class="pa-1" />
          </v-avatar>
          <!-- <label>{{ item.name }}</label> -->
          <v-chip
            label
            color="blue lighten-5"
            text-color="blue darken-4"
          >
            {{ item.name }}
          </v-chip>
        </template>
      </v-data-table>
    </v-card>
    <UserDialog :dialog="userDialog" :userInfo="userInfo" @close="userDialog=false"/>
  </div>
</template>
<script>
import { mapActions } from 'vuex'
import UserDialog from '@/components/UserDialog.vue';
export default {
  components: {
    UserDialog
  },
  data() {
    return {
      headers: [
        { text: 'id', value: 'id' },
        { text: '氏名', value: 'name' },
      ],
      desserts: [
        { id: 1, name: 'AAA' },
        { id: 2, name: 'BBB' },
        { id: 3, name: 'CCC' },
      ],
      userDialog: false,
      imgPath: require('@/assets/user.jpg'),
      userInfo: {}
    }
  },

  methods: {
    ...mapActions('user', ['changeUser']),

    search() {
      // TODO 一覧検索
    },

    clickRow(item) {
      this.changeUser(item);
      this.userDialog = true;
    },

    clickNew() {
      this.changeUser({});
      this.userDialog = true;
    }
  }
}
</script>