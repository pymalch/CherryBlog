<%inherit file="master.mak"/>

<%def name="title()">${page_title}</%def>

% if 'MESSAGE' in cherrypy.session :
<div class="message">

    ${cherrypy.session['MESSAGE']}

</div>
<% cherrypy.session.pop('MESSAGE') %>
% endif

    <%include file="userPanel.mak"/>


<section class="posts">
    % for post in posts:
    <article data-id="${post.id}">
        <header>
            % if loop.index==0:
              <h1 class="postTitle"> ${post.title} </h1>
             % else:
             <h2 class="postTitle"> ${post.title} </h2>
            % endif
        </header>

       <div class="content">${post.content}</div>
        <time>${post.entry_time.strftime('%Y/%m/%d %H:%M')}</time>

    </article>
    % endfor
</section>

% if  cherrypy.session.get('_cp_username')!=None:
    <%include file="blogPanel.mak"/>
% endif

