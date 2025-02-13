Name:		texlive-lewis
Version:	15878
Release:	2
Summary:	Draw Lewis structures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lewis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
