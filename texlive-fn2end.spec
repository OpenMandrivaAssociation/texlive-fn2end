# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fn2end
# catalog-date 2009-01-03 10:55:55 +0100
# catalog-license pd
# catalog-version 1.1
Name:		texlive-fn2end
Version:	1.1
Release:	4
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751984
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718469
- texlive-fn2end
- texlive-fn2end
- texlive-fn2end
- texlive-fn2end

