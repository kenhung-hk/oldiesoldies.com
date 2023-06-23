def generate_html(project_url, project_title, branding_title, image_url,view_str):
    html = f'''
    <section class="grid-item filter_branding filter_featured filter_illustration filter_works filter_post-format-gallery"
             data-postid="170">
        <div class="grid-item-inside">
            <div class="grid-item-con">
                <a href="{project_url}" title="{project_title}"
                    class="grid-item-mask-link grid-item-open-url"></a>
                <div class="grid-item-con-text">
                    <span class="grid-item-cate">
                        <a href="#" title="View all posts in {branding_title}" class="grid-item-cate-a"
                            data-filter=".filter_branding">{branding_title}</a>
                        <a href="#" title="View all posts in Illustration" class="grid-item-cate-a"
                            data-filter=".filter_illustration">Illustration</a>
                    </span>
                    <h2 class="grid-item-tit">
                        <a href="{project_url}" title="{project_title}" class="grid-item-tit-a">{project_title}</a>
                    </h2>
                </div>
            </div>
            <div class="brick-content ux-lazyload-wrap" style="padding-top: 75.384615384615%;">
                <div class="ux-lazyload-bgimg ux-background-img" data-bg="{image_url}"></div>
            </div>
        </div><!--End inside-->
    </section>
    '''
    return html
#  Aldi Sourcing Asia Limited 1-6 Work Experience
# Oldies’oldies 7 - 16  My e-Commerce Business
# Hong Kong Young Fashion designer's contest 2019 17 - 33 - Competitions and Awards
# Final Year project  34 - 46 -  School Projects
# XINAO KNIT FOR NEXT COMPETITION 2018 47-55 - Competitions and Awards
# Knitwear deisgn Project Brand Study 56-75 - School Projects
# 40th ANNIVERARY SOUVENIR FOR BUDDHIST WONG WAN TIN COLLEGE 76-78 Work Experience