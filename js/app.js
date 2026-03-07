const app = {
    currentView: "inicio",
    // Base de datos de juegos con URLs de itch.io integradas
    games: [
        { 
            id: "InkSiege", 
            name: "INKSIEGE", 
            type: "TACTICAL_STEALTH", 
            img: "https://raw.githubusercontent.com/BluePandaOpn/InkSiege-Docs/main/assets/logo.png",
            url: "https://pato404.itch.io/ink-survivors-paper-siege",
            description: "Sobrevive al asedio de papel en este shooter táctico minimalista."
        },
        { 
            id: "WheelieLife", 
            name: "Wheelie Life", 
            type: "CYBERPUNK_RPG", 
            img: "https://img.itch.zone/aW1nLzI1MjM1NDkzLnBuZw==/original/gdASWm.png",
            url: "https://pato404.itch.io/wheelie-life",
            description: "Domina las calles en un futuro distópico sobre dos ruedas."
        }
    ],

    sectionPaths: {
        inicio: "html/inicio.html",
        juegos: "html/juegos.html",
        estudio: "html/estudio.html",
        contacto: "html/contacto.html"
    },

    async init() {
        this.applySavedTheme();
        this.bindHeaderEvents();
        this.handleScroll(); // Se eliminó handleCursor para usar el ratón normal
        window.addEventListener("hashchange", () => this.syncWithHash());
        await this.syncWithHash();
        lucide.createIcons();
    },

    async syncWithHash() {
        const hash = (window.location.hash || "#inicio").replace("#", "");
        const view = this.sectionPaths[hash] ? hash : "inicio";
        await this.navigate(view, false);
    },

    async navigate(viewId, updateHash = true) {
        if (!this.sectionPaths[viewId]) return;

        this.currentView = viewId;
        this.setActiveNav(viewId);
        await this.loadView(viewId);
        this.bindViewEvents();
        this.revealOnScroll();
        window.scrollTo({ top: 0, behavior: "smooth" });

        if (updateHash) window.location.hash = viewId;

        const header = document.getElementById("nav-header");
        header.classList.remove("menu-open");
        lucide.createIcons();
    },

    async loadView(viewId) {
        const root = document.getElementById("app-content");
        root.innerHTML = `
            <div class="loader-container">
                <div class="spinner"></div>
                <p>ACCEDIENDO AL SISTEMA...</p>
            </div>`;

        try {
            const res = await fetch(this.sectionPaths[viewId]);
            if (!res.ok) throw new Error("No se pudo cargar la sección");

            root.innerHTML = await res.text();
            if (viewId === "juegos") this.renderGames();

        } catch (error) {
            root.innerHTML = "<section class='view'><p>Error crítico de conexión.</p></section>";
        }
    },

    // Renderizado con redirección funcional a Itch.io
    renderGames() {
        const container = document.getElementById("game-container");
        if (!container) return;

        container.innerHTML = this.games.map((g) => `
            <article class="card-elite reveal" onclick="window.open('${g.url}', '_blank')" style="cursor: pointer;">
                <div class="card-img">
                    <img src="${g.img}" alt="${g.name}" loading="lazy">
                    <div class="card-overlay">
                         <div class="btn-install">
                            <i data-lucide="download"></i> INSTALAR
                         </div>
                    </div>
                </div>
                <div class="card-content">
                    <div class="card-head">
                        <span class="file-id">FILE_ID: ${g.id}</span>
                        <span class="chip">${g.type}</span>
                    </div>
                    <h3>${g.name}</h3>
                    <p>${g.description || "Misión crítica de desarrollo para plataformas de nueva generación."}</p>
                    <div class="card-footer">
                        <button class="btn-secondary">
                            VER EN ITCH.IO
                        </button>
                    </div>
                </div>
            </article>
        `).join("");
        lucide.createIcons();
    },

    bindHeaderEvents() {
        const themeBtn = document.getElementById("theme-toggle");
        const menuBtn = document.getElementById("menu-toggle");
        const logo = document.querySelector(".logo");

        themeBtn.addEventListener("click", () => this.toggleTheme());
        menuBtn.addEventListener("click", () => {
            document.getElementById("nav-header").classList.toggle("menu-open");
        });
        logo.addEventListener("click", () => this.navigate("inicio"));

        document.querySelectorAll(".nav-link").forEach((link) => {
            link.addEventListener("click", async (event) => {
                event.preventDefault();
                const nextView = link.getAttribute("data-view");
                await this.navigate(nextView);
            });
        });
    },

    bindViewEvents() {
        document.querySelectorAll("[data-view]").forEach((button) => {
            button.addEventListener("click", async (event) => {
                if (button.tagName === "A") event.preventDefault();
                const nextView = button.getAttribute("data-view");
                await this.navigate(nextView);
            });
        });

        const form = document.getElementById("contact-form");
        if (form) {
            form.addEventListener("submit", (event) => this.submitForm(event));
        }
    },

    setActiveNav(viewId) {
        document.querySelectorAll(".nav-link").forEach((link) => {
            link.classList.toggle("active", link.getAttribute("data-view") === viewId);
        });
    },

    handleScroll() {
        window.addEventListener("scroll", () => {
            const header = document.getElementById("nav-header");
            header.classList.toggle("scrolled", window.scrollY > 90);
            this.revealOnScroll();
        });
    },

    revealOnScroll() {
        document.querySelectorAll(".reveal").forEach((el) => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight - 80) {
                el.classList.add("active");
            }
        });
    },

    applySavedTheme() {
        const savedTheme = localStorage.getItem("bp-theme") || "dark";
        document.body.setAttribute("data-theme", savedTheme);
        this.syncThemeIcon();
    },

    toggleTheme() {
        const body = document.body;
        const isDark = body.getAttribute("data-theme") === "dark";
        const nextTheme = isDark ? "light" : "dark";
        body.setAttribute("data-theme", nextTheme);
        localStorage.setItem("bp-theme", nextTheme);
        this.syncThemeIcon();
    },

    syncThemeIcon() {
        const isDark = document.body.getAttribute("data-theme") === "dark";
        const icon = document.getElementById("theme-ico");
        if(icon) {
            icon.setAttribute("data-lucide", isDark ? "sun" : "moon");
            lucide.createIcons();
        }
    },

    submitForm(event) {
        event.preventDefault();
        const button = event.target.querySelector("button[type='submit']");
        button.disabled = true;
        button.textContent = "ENVIANDO DATOS...";
        setTimeout(() => {
            button.disabled = false;
            button.innerHTML = "DATOS RECIBIDOS <i data-lucide='check'></i>";
            lucide.createIcons();
            event.target.reset();
        }, 1500);
    }
};

window.addEventListener("load", () => {
    app.init();
});