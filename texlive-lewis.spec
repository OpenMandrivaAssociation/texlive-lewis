# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lewis
# catalog-date 2007-03-08 21:58:53 +0100
# catalog-license pd
# catalog-version 0.1
Name:		texlive-lewis
Version:	0.1
Release:	5
Summary:	Draw Lewis structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lewis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides rudimentary support for drawing Lewis
Structures. Support is limited to elements that support the
octet rule.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lewis/lewis.sty
%doc %{_texmfdistdir}/doc/latex/lewis/README
%doc %{_texmfdistdir}/doc/latex/lewis/lewis.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 753296
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 718848
- texlive-lewis
- texlive-lewis
- texlive-lewis
- texlive-lewis

