// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package doppler

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-doppler/sdk/go/doppler/internal"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "doppler:index/config:Config":
		r = &Config{}
	case "doppler:index/environment:Environment":
		r = &Environment{}
	case "doppler:index/project:Project":
		r = &Project{}
	case "doppler:index/secret:Secret":
		r = &Secret{}
	case "doppler:index/serviceToken:ServiceToken":
		r = &ServiceToken{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:doppler" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"doppler",
		"index/config",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"index/environment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"index/project",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"index/secret",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"index/serviceToken",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"doppler",
		&pkg{version},
	)
}
