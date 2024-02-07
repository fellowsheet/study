async function getAllPosts() {
    const res = await fetch('http://127.0.0.1:8000/posts/?limit=10');
    const posts = await res.json();

    console.log(posts);
    posts.forEach(post => postToHTML(post));
}

window.addEventListener('DOMContentLoaded', getAllPosts);

function postToHTML({id, title, content, author, published}) {
    const postList = document.getElementById('posts');

    postList.insertAdjacentHTML('beforeend', `
        <article class="media content-section">
            <div class="media-body">
                <div class="article-metadata" id="post${id}">
                    <a class="mr-2" href="#">${author}</a>
                    <small class="text-muted">${published}</small>
                </div>
                    <h2><a class="article-title" href="#">${title}</a></h2>
                    <p class="article-content">${content}</p>
            </div>
        </article>
    `);
}