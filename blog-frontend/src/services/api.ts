import axios from 'axios';

const CORE_API_URL = import.meta.env.VITE_CORE_API_URL;
const COMMENT_API_URL = import.meta.env.VITE_COMMENT_API_URL;

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

export const createBlogPost = (data: Partial<any>) => 
  coreApi.post('/posts/', data);

export const updateBlogPost = (id: number, data: Partial<any>) => 
  coreApi.put(`/posts/${id}/`, data);

export const deleteBlogPost = (id: number) => 
  coreApi.delete(`/posts/${id}/`);

const commentApi = axios.create({
  baseURL: COMMENT_API_URL,
});

commentApi.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const getCommentsByPost = (postId: number, page = 1) => 
  commentApi.get('/comments/', { params: { post_id: postId, page } });

export const getCommentsByUser = (userId: number, page = 1) => 
  commentApi.get('/comments/', { params: { user_id: userId, page } });

export const createComment = (data: Partial<any>) => 
  commentApi.post('/comments/', data);

export const updateComment = (id: number, data: Partial<any>) => 
  commentApi.put(`/comments/${id}/`, data);

export const deleteComment = (id: number) => 
  commentApi.delete(`/comments/${id}/`);
