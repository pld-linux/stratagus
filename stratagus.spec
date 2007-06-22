#
# TODO:
# - OpenGL into seperate package (game doesnt works compiled --with-opengl
#   on non opengl supported)
#
Summary:	Free cross-platform real-time strategy gaming engine
Summary(pl.UTF-8):	Darmowy, wieloplatformowy silnik gier strategicznych czasu rzeczywistego
Name:		stratagus
Version:	2.2.4
Release:	1
License:	GPL v2+
Group:		Applications/Games/Strategy
Vendor:		Stratagus Team
Source0:	http://dl.sourceforge.net/stratagus/%{name}-%{version}-src.tar.gz
# Source0-md5:	311b41c8dcd2d695d2f3ca7d2c17587e
Patch0:		%{name}-includepaths.patch
URL:		http://stratagus.sourceforge.net/
#BuildRequires:	XFree86-devel
BuildRequires:	SDL-devel
BuildRequires:	bzip2-devel
BuildRequires:	flac-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	linux-libc-headers
BuildRequires:	lua50-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a
computer opponent. The engine is configurable and can be used to
create games with a wide-range of features specific to your needs. See
the data sets page for a list of current games using the stratagus
engine.

It is highly active in development and usage.

%description -l pl.UTF-8
Stratagus to darmowy, wieloplatformowy silnik gier strategicznych
czasu rzeczywistego. Zawiera obsługę grania przez internet lub w sieci
lokalnej, oraz grania przeciwko komputerowi. Silnik jest
konfigurowalny i może być używany do tworzenia gier o wielu cechach
specyficznych dla naszych potrzeb. Aktualna lista gier używających
silnika stratagus znajduje się na stronie "data sets".

Projekt jest bardzo aktywny pod względem rozwoju i wykorzystania.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-x \
	--with-bzip2 \
	--with-ogg \
	--with-mikmod \
	--with-mad \
	--with-flac \
	--with-cdaudio=sdlcd \
	--with-lua
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install stratagus $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/*
