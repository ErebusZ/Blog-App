import axios from 'axios';

const CORE_API_URL = 'https://Core-api.com';

const coreApi = axios.create({
  baseURL: CORE_API_URL,
});

coreApi.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const login = (username: string, password: string) => 
    coreApi.post('/login/', { username, password });

export const register = (username: string, email: string, password: string, firstName: string, lastName: string) => 
    coreApi.post('/register/', { username, email, password, firstName, lastName });

export const getBlogPosts = (page: number = 1, search: string = '') => 
    coreApi.get('/posts/', { params: { page, search } });

export const getBlogPost = (id: number) => 
    coreApi.get(`/posts/${id}/`);

export const createBlogPost = (data: Partial<BlogPost>) => 
    coreApi.post('/posts/', data);

export const updateBlogPost = (id: number, data: Partial<BlogPost>) => 
    coreApi.put(`/posts/${id}/`, data);

export const deleteBlogPost = (id: number) => 
    coreApi.delete(`/posts/${id}/`);

