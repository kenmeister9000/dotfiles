(setq inhibit-startup-message t) ; Don't Show Splash Screen
(setq visible-bell t) ; Flash When Bell Rings
(setq dashboard-center-content t) ; Centers Dashboard Content
(global-display-line-numbers-mode 1)
(hl-line-mode 1)
(scroll-bar-mode -1)
(load-theme 'dracula t) 
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(doom-modeline-enable-word-count t)
 '(package-selected-packages
   '(all-the-icons dashboard doom-modeline dracula-theme org-modern
		   vertico-posframe)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
;; Comment/uncomment this line to enable MELPA Stable if desired.  See `package-archive-priorities`
;; and `package-pinned-packages`. Most users will not need or want to do this.
;;(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(package-initialize) 

(use-package vertico
:custom
   (vertico-scroll-margin 0) ;; Different scroll margin
   (vertico-count 20) ;; Show more candidates
   (vertico-resize t) ;; Grow and shrink the Vertico minibuffer
   (vertico-cycle t) ;; Enable cycling for `vertico-next/previous'
  :init
  (vertico-mode))

(use-package savehist
  :init
  (savehist-mode))

(use-package all-the-icons
  :if (display-graphic-p))

(use-package doom-modeline
  :ensure t
  :init (doom-modeline-mode 1)) 

(use-package dashboard
  :ensure t
  :config
  (dashboard-setup-startup-hook))
(with-eval-after-load 'org (global-org-modern-mode))
