// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package integration

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
	case "doppler:integration/awsParameterStore:AwsParameterStore":
		r = &AwsParameterStore{}
	case "doppler:integration/awsSecretsManager:AwsSecretsManager":
		r = &AwsSecretsManager{}
	case "doppler:integration/flyio:Flyio":
		r = &Flyio{}
	case "doppler:integration/terraformCloud:TerraformCloud":
		r = &TerraformCloud{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"doppler",
		"integration/awsParameterStore",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"integration/awsSecretsManager",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"integration/flyio",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"doppler",
		"integration/terraformCloud",
		&module{version},
	)
}
