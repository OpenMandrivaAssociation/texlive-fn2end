Name:		texlive-fn2end
Version:	15878
Release:	1
Summary:	Convert footnotes to endnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fn2end
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fn2end.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fn2end.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines macros \makeendnotes, which converts \footnote to
produce endnotes; and \theendnotes which prints them out.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fn2end/fn2end.sty
%doc %{_texmfdistdir}/doc/latex/fn2end/fn2end.pdf
%doc %{_texmfdistdir}/doc/latex/fn2end/fn2end.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
