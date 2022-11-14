import axios from "axios"

const AxiosPlugin = {}

AxiosPlugin.install = function (Vue) {
  Vue.prototype.$axios = axios.create({
    baseURL: process.env.VUE_APP_API_BASE_URL,
    headers: {
      'Content-Type': 'application/json'
    },
    responseType: 'json',
    timeout: 3000
  })

  // リクエストログ
  Vue.prototype.$axios.interceptors.request.use(
    function (config) {
      console.info(config)
      return config;
    },
    function (error) {
      console.error(error)
      return Promise.reject(error);
    }
  )

  // レスポンスログ
  Vue.prototype.$axios.interceptors.response.use(
    function (response) {
      console.info(response)
      return response;
    },
    function (error) {
      console.error(error)
      return Promise.reject(error);
    }
  )
}

export default AxiosPlugin;