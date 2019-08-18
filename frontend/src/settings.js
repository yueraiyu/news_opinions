import axios from 'axios'

// 基础配置
axios.defaults.timeout = 5000  // 超时时间
axios.defaults.baseURL = 'http://127.0.0.1:8098'

export default axios
