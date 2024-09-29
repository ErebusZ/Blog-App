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
author_id: number;
blog_id: number;
created_at: string;
}