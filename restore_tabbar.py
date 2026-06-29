import os

pages = [
    ('C:/Users/Administrator/Desktop/Entertainment/pages/news/news.uvue', 'pages/news/news'),
    ('C:/Users/Administrator/Desktop/Entertainment/pages/index/index.uvue', 'pages/index/index'),
    ('C:/Users/Administrator/Desktop/Entertainment/pages/performance/performance.uvue', 'pages/performance/performance'),
    ('C:/Users/Administrator/Desktop/Entertainment/pages/service-tab/service-tab.uvue', 'pages/service-tab/service-tab'),
    ('C:/Users/Administrator/Desktop/Entertainment/pages/mine/mine.uvue', 'pages/mine/mine'),
]

tab_tag = '\t<custom-tab-bar active="{}" />\n</template>'
import_line = "import customTabBar from '../../components/custom-tab-bar/custom-tab-bar.uvue'\n<script setup"

for filepath, page_path in pages:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'custom-tab-bar' not in content:
        # Add custom-tab-bar tag before </template>
        tag = tab_tag.format(page_path)
        content = content.replace('</template>', tag)
        
        # Add import after <script setup
        if '<script setup' in content:
            content = content.replace('<script setup', import_line)
        
        # Add padding-bottom for pages that have .container
        if '.container {' in content and 'padding-bottom' not in content:
            content = content.replace('.container {', '.container {\n\t\tpadding-bottom: 120rpx;')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Restored:', os.path.basename(filepath))
    else:
        print('Already has:', os.path.basename(filepath))
