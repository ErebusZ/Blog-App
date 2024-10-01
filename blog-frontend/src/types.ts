export interface BlogPost {
  id: number;
  title: string;
  author?: number;
  content: string;
  image?: string;
  userId: number;
}

export interface User {
  id: number;
  name: string;
}
