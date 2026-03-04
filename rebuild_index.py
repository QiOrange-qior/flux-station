import os

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Flux Station - Creative Platform</title>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
<script>
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: "#6366F1",
                        "background-light": "#F9F9FB",
                        "background-dark": "#0F0F12",
                        "surface-light": "#FFFFFF",
                        "surface-dark": "#18181B",
                        "text-main-light": "#111827",
                        "text-main-dark": "#F3F4F6",
                        "text-muted-light": "#6B7280",
                        "text-muted-dark": "#9CA3AF",
                        "accent-lavender": "#E9E5FF",
                        "accent-mint": "#DDFBF3",
                        "accent-sky": "#E0F2FE",
                        "glass-border-light": "rgba(255, 255, 255, 0.6)",
                        "glass-border-dark": "rgba(255, 255, 255, 0.1)",
                        "iris-start": "#6366F1",
                        "iris-end": "#A855F7",
                    },
                    fontFamily: {
                        serif: ['"Instrument Serif"', 'serif'],
                        sans: ['"Inter"', 'sans-serif'],
                    },
                    boxShadow: {
                        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)',
                        'floating': '0 20px 40px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
                        'glow-primary': '0 0 15px rgba(99, 102, 241, 0.5), 0 0 30px rgba(99, 102, 241, 0.3)',
                        'deep': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
                    },
                    backdropBlur: {
                        'xs': '2px',
                    },
                    animation: {
                        'shimmer-text': 'shimmer 3s linear infinite',
                        'liquid-pulse': 'liquidPulse 2s infinite',
                        'spin-slow': 'spin 3s linear infinite',
                    },
                    keyframes: {
                        shimmer: {
                            '0%': { backgroundPosition: '-200% center' },
                            '100%': { backgroundPosition: '200% center' },
                        },
                        liquidPulse: {
                            '0%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(99, 102, 241, 0.7)' },
                            '70%': { transform: 'scale(1.02)', boxShadow: '0 0 0 10px rgba(99, 102, 241, 0)' },
                            '100%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(99, 102, 241, 0)' },
                        }
                    }
                },
            },
        };
    </script>
<style type="text/tailwindcss">
        body {
            font-family: 'Inter', sans-serif;
        }
        .font-serif {
            font-family: 'Instrument Serif', serif;
        }
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #E5E7EB;
            border-radius: 3px;
        }
        .dark ::-webkit-scrollbar-thumb {
            background: #374151;
        }
        .gradient-card-1 {
            background: linear-gradient(135deg, #E9E5FF 0%, #FAD0C4 100%);
        }
        .gradient-card-2 {
            background: linear-gradient(135deg, #ABDCFF 0%, #FFD1FF 100%);
        }
        .gradient-card-3 {
            background: linear-gradient(135deg, #DDFBF3 0%, #E9E5FF 100%);
        }
        .text-iris-gradient {
            background: linear-gradient(to right, #6366F1, #A855F7, #EC4899, #6366F1);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .nav-link {
            position: relative;
        }
        .nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #6366F1, #A855F7, #EC4899);
            transition: width 0.3s ease;
            opacity: 0.7;
        }
        .nav-link:hover::after {
            width: 100%;
        }
        .toggle-checkbox:checked {
            right: 0;
            border-color: #6366F1;
        }
        .toggle-checkbox:checked + .toggle-label {
            background-color: #6366F1;
        }

        /* Screen 3 Modal Styles */
        .glass-panel {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow:
                0 4px 6px -1px rgba(0, 0, 0, 0.05),
                0 2px 4px -1px rgba(0, 0, 0, 0.03),
                0 0 0 1px rgba(255,255,255,0.5),
                0 20px 60px -10px rgba(99, 102, 241, 0.1);
        }
        .dark .glass-panel {
            background: rgba(24, 24, 27, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 60px -10px rgba(0, 0, 0, 0.5);
        }
        .segmented-control {
            background: #F3F4F6;
            border-radius: 12px;
            padding: 4px;
            display: inline-flex;
            width: 100%;
        }
        .segmented-option {
            flex: 1;
            text-align: center;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.875rem;
            color: #6B7280;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }
        .segmented-option.selected {
            background: white;
            color: #6366F1;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            font-weight: 600;
        }
        .master-switch .segmented-option.selected {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }
        .ratio-btn {
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            font-size: 0.875rem;
            color: #4B5563;
            transition: all 0.2s;
            background: rgba(255,255,255,0.5);
        }
        .ratio-btn:hover {
            border-color: #6366F1;
            color: #6366F1;
            background: white;
        }
        .ratio-btn.selected {
            background: #6366F1;
            border-color: transparent;
            color: white;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }
        .aesthetic-card {
            border-radius: 12px;
            padding: 0.75rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: 500;
            font-size: 0.85rem;
            color: #1F2937;
            border: 1px solid transparent;
            transition: all 0.2s;
            height: 80px;
            position: relative;
            overflow: hidden;
            text-align: center;
        }
        .aesthetic-card:hover {
             transform: translateY(-2px);
             box-shadow: 0 8px 16px rgba(99, 102, 241, 0.1);
        }
        .dashed-upload {
            background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='12' ry='12' stroke='%236366F1' stroke-width='2' stroke-dasharray='6%2c 6' stroke-dashoffset='0' stroke-linecap='round'/%3e%3c/svg%3e");
            background-color: rgba(99, 102, 241, 0.03);
        }
        .bg-gradient-cinematic { background: linear-gradient(135deg, #FDE68A 0%, #FCA5A5 100%); }
        .bg-gradient-ethereal { background: linear-gradient(135deg, #E9D5FF 0%, #DDD6FE 100%); }
        .bg-gradient-fluid { background: linear-gradient(135deg, #A7F3D0 0%, #6EE7B7 100%); }
        .bg-gradient-minimal { background: linear-gradient(135deg, #F3F4F6 0%, #E5E7EB 100%); }
        .bg-gradient-fantasy { background: linear-gradient(135deg, #C4B5FD 0%, #A78BFA 100%); color: white !important; }
        .bg-gradient-cyber { background: linear-gradient(135deg, #F9A8D4 0%, #F472B6 100%); color: white !important; }
        .bg-no-style { background: #F3F4F6; border: 1px solid #E5E7EB; color: #6B7280; }
        .dark .bg-no-style { background: #18181B; border: 1px solid #27272A; color: #9CA3AF; }
        .aesthetic-card.selected {
            border: 2px solid #6366F1;
            box-shadow: 0 0 12px rgba(99, 102, 241, 0.3);
        }
        .aesthetic-card.selected::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 10px;
            border: 2px solid transparent;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%) border-box;
            -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: destination-out;
            mask-composite: exclude;
            pointer-events: none;
        }
        #reference-section {
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            max-height: 0;
            opacity: 0;
            overflow: hidden;
            margin-top: 0;
        }
        #reference-section.active {
            max-height: 300px;
            opacity: 1;
            margin-top: 2rem;
        }

        /* Modal Content Scrollbar */
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #E5E7EB;
            border-radius: 4px;
        }

        .masonry-grid-models {
            column-count: 3;
            column-gap: 1.5rem;
        }
        .masonry-item-models {
            break-inside: avoid;
        }
        @media (max-width: 1024px) {
            .masonry-grid-models { column-count: 2; }
        }
        @media (max-width: 640px) {
            .masonry-grid-models { column-count: 1; }
        }
        @keyframes floatIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Asset Detail Styles */
        .iris-border {
            position: relative;
        }
        .iris-border::before {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: inherit;
            padding: 2px;
            background: linear-gradient(45deg, #6366F1, #A855F7);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            opacity: 0.6;
        }
        .shadow-glow-iris {
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.2), 0 0 40px rgba(168, 85, 247, 0.1);
        }
    </style>
</head>
<body class="bg-background-light dark:bg-background-dark text-text-main-light dark:text-text-main-dark h-screen w-screen overflow-hidden flex selection:bg-primary selection:text-white transition-colors duration-300">

<!-- SIDEBAR -->
<aside class="w-64 flex-shrink-0 flex flex-col justify-between border-r border-gray-200 dark:border-gray-800 bg-surface-light/80 dark:bg-surface-dark/80 backdrop-blur-md z-20 h-full relative">
    <div class="p-6">
        <div class="mb-8">
            <h1 class="font-serif text-4xl text-text-main-light dark:text-text-main-dark tracking-tight">Flux station</h1>
            <p class="text-[10px] uppercase tracking-widest text-text-muted-light dark:text-text-muted-dark font-medium mt-1">Creative Engine</p>
        </div>
        <nav class="space-y-1">
            <a id="nav-gen" class="flex items-center px-3 py-2.5 text-sm font-medium rounded-xl bg-white dark:bg-gray-800 shadow-sm border border-gray-100 dark:border-gray-700 text-primary group transition-all" href="javascript:void(0)" onclick="switchView('gen')">
                <span class="material-symbols-outlined mr-3 text-[20px]">auto_awesome</span>
                素材生成
            </a>
            <a id="nav-video" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView('video')">
                <span class="material-symbols-outlined mr-3 text-[20px]">movie</span>
                视频生成
            </a>
            <a id="nav-plaza" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView('plaza')">
                <span class="material-symbols-outlined mr-3 text-[20px]">grid_view</span>
                模型广场
            </a>
            <a id="nav-api" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView('api')">
                <span class="material-symbols-outlined mr-3 text-[20px]">api</span>
                API管理
            </a>
            <a id="nav-vault" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView('vault')">
                <span class="material-symbols-outlined mr-3 text-[20px]">folder_special</span>
                资产
            </a>
        </nav>
    </div>

    <div class="p-4 border-t border-gray-100 dark:border-gray-800">
        <div class="flex justify-between items-center mb-2">
            <span class="text-xs font-medium text-text-muted-light dark:text-text-muted-dark">存储空间</span>
            <span class="text-xs font-medium text-text-main-light dark:text-text-main-dark">已用 12%</span>
        </div>
        <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mt-1">
            <div class="bg-primary h-1.5 rounded-full" style="width: 12%"></div>
        </div>
    </div>
    <div class="p-4 border-t border-gray-100 dark:border-gray-800">
        <div class="flex items-center justify-between px-1">
            <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px] text-yellow-500 animate-spin-slow" style="animation-duration: 10s;">light_mode</span>
                <label class="relative inline-flex items-center cursor-pointer group">
                    <input class="sr-only peer" type="checkbox" value=""/>
                    <div class="w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-2 peer-focus:ring-primary dark:peer-focus:ring-primary rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-600 peer-checked:bg-primary"></div>
                </label>
                <span class="material-symbols-outlined text-[18px] text-gray-400 group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors">dark_mode</span>
            </div>
        </div>
    </div>
</aside>
''')
