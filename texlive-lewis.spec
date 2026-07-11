%global tl_name lewis
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Draw Lewis structures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lewis
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides rudimentary support for drawing Lewis Structures.
Support is limited to elements that support the octet rule.

