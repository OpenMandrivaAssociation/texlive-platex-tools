Name:		texlive-platex-tools
Version:	72097
Release:	1
Summary:	pLaTeX standard tools bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/platex-tools
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platex-tools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platex-tools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle is an extended version of the latex-tools bundle
developed by the LaTeX team, mainly intended to support
pLaTeX2e and upLaTeX2e. Currently patches for the latex-tools
bundle and Martin Schroder's ms bundle are included.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/platex-tools
%doc %{_texmfdistdir}/doc/latex/platex-tools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
