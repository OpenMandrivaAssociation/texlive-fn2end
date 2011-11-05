# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fn2end
# catalog-date 2009-01-03 10:55:55 +0100
# catalog-license pd
# catalog-version 1.1
Name:		texlive-fn2end
Version:	1.1
Release:	1
Summary:	Convert footnotes to endnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fn2end
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fn2end.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fn2end.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines macros \makeendnotes, which converts \footnote to
produce endnotes; and \theendnotes which prints them out.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fn2end/fn2end.sty
%doc %{_texmfdistdir}/doc/latex/fn2end/fn2end.pdf
%doc %{_texmfdistdir}/doc/latex/fn2end/fn2end.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
