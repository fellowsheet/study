function clear() {
    document.getElementById('content-block').innerHTML = '';
}

async function getAllPosts() {
    const res = await fetch('http://127.0.0.1:8000/posts/?limit=10');
    const posts = await res.json();

    console.log(posts);
    posts.forEach(post => postToHTML(post));
}

window.addEventListener('DOMContentLoaded', getAllPosts);

function postToHTML({id, title, content, author, published}) {
    const postList = document.getElementById('content-block');
    const publishedDate = new Date(published).toLocaleString();

    postList.insertAdjacentHTML('beforeend', `
        <article class="media content-section">
            <div class="media-body">
                <div class="article-metadata" id="post${id}">
                    <a class="mr-2" href="#">${author}</a>
                    <small class="text-muted">${publishedDate}</small>
                </div>
                    <h2><a class="article-title" href="#">${title}</a></h2>
                    <p class="article-content">${content}</p>
            </div>
        </article>
    `);
}

async function getAllAuthors() {
    const res = await fetch('http://127.0.0.1:8000/authors/?limit=10');
    const authors = await res.json();

    console.log(authors);
    authors.forEach(author => authorToHTML(author));
}

function authorToHTML({id, first_name, last_name, avatar, birth_date, slug}) {
    const authorList = document.getElementById('content-block');

    authorList.insertAdjacentHTML('beforeend', `
        <div class="content-section" id="author{id}">
            <div class="media">
                <img class="rounded-circle account-img" src="${avatar}">
                <div class="media-body">
                    <h4 class="account-heading">${first_name} ${last_name}</h4>
                    <p>${birth_date}</p>
                    <p class="text-secondary">${slug}</p>
                </div>
            </div>
        </div>
    `);
}

window.addEventListener("click", function(e){
    if (e.target.id=="all_authors"){
        clear();
        getAllAuthors();
    }
})

window.addEventListener("click", function(e){
    if (e.target.id=="all_posts"){
        clear();
        getAllPosts();
    }
})