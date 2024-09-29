export interface User {
id: number;
username: string;
email: string;
}
  
export interface BlogPost {
id: number;
title: string;
content: string;
author: User;
created_at: string;
updated_at: string;
}

export interface Comment {
id: number;
content: string;
author: User;
blog_post: number;
created_at: string;
}