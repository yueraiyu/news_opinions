import axios from 'axios'

// 基础配置
axios.defaults.timeout = 5000  // 超时时间
axios.defaults.baseURL = 'http://localhost:5000'

export default axios
