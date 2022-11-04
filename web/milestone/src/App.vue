<template>
  <v-app>
    <!-- サイドメニュー -->
    <v-navigation-drawer app clipped v-model="drawer" color="white">
      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.url"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- ヘッダー -->
    <v-app-bar app clippedLeft flat dark color="indigo darken-3">
      <v-app-bar-nav-icon @click.stop="drawer=!drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <!-- メイン -->
    <v-main class="blue-grey lighten-5">
      <v-container style="padding: 30px 120px;">
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        drawer: true,
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', url: '/' },
          { title: 'Users', icon: 'mdi-image', url: '/users' },
          { title: 'Milestone', icon: 'mdi-help-box', url: '/milestone' },
        ]
      }
    }
  }
</script>

<style>
</style>
