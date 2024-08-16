// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { BranchConfigArgs, BranchConfigState } from "./branchConfig";
export type BranchConfig = import("./branchConfig").BranchConfig;
export const BranchConfig: typeof import("./branchConfig").BranchConfig = null as any;
utilities.lazyLoad(exports, ["BranchConfig"], () => require("./branchConfig"));

export { EnvironmentArgs, EnvironmentState } from "./environment";
export type Environment = import("./environment").Environment;
export const Environment: typeof import("./environment").Environment = null as any;
utilities.lazyLoad(exports, ["Environment"], () => require("./environment"));

export { GetSecretsArgs, GetSecretsResult, GetSecretsOutputArgs } from "./getSecrets";
export const getSecrets: typeof import("./getSecrets").getSecrets = null as any;
export const getSecretsOutput: typeof import("./getSecrets").getSecretsOutput = null as any;
utilities.lazyLoad(exports, ["getSecrets","getSecretsOutput"], () => require("./getSecrets"));

export { GetUserArgs, GetUserResult, GetUserOutputArgs } from "./getUser";
export const getUser: typeof import("./getUser").getUser = null as any;
export const getUserOutput: typeof import("./getUser").getUserOutput = null as any;
utilities.lazyLoad(exports, ["getUser","getUserOutput"], () => require("./getUser"));

export { GroupArgs, GroupState } from "./group";
export type Group = import("./group").Group;
export const Group: typeof import("./group").Group = null as any;
utilities.lazyLoad(exports, ["Group"], () => require("./group"));

export { GroupMemberArgs, GroupMemberState } from "./groupMember";
export type GroupMember = import("./groupMember").GroupMember;
export const GroupMember: typeof import("./groupMember").GroupMember = null as any;
utilities.lazyLoad(exports, ["GroupMember"], () => require("./groupMember"));

export { ProjectArgs, ProjectState } from "./project";
export type Project = import("./project").Project;
export const Project: typeof import("./project").Project = null as any;
utilities.lazyLoad(exports, ["Project"], () => require("./project"));

export { ProjectRoleArgs, ProjectRoleState } from "./projectRole";
export type ProjectRole = import("./projectRole").ProjectRole;
export const ProjectRole: typeof import("./projectRole").ProjectRole = null as any;
utilities.lazyLoad(exports, ["ProjectRole"], () => require("./projectRole"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SecretArgs, SecretState } from "./secret";
export type Secret = import("./secret").Secret;
export const Secret: typeof import("./secret").Secret = null as any;
utilities.lazyLoad(exports, ["Secret"], () => require("./secret"));

export { ServiceAccountArgs, ServiceAccountState } from "./serviceAccount";
export type ServiceAccount = import("./serviceAccount").ServiceAccount;
export const ServiceAccount: typeof import("./serviceAccount").ServiceAccount = null as any;
utilities.lazyLoad(exports, ["ServiceAccount"], () => require("./serviceAccount"));

export { ServiceAccountTokenArgs, ServiceAccountTokenState } from "./serviceAccountToken";
export type ServiceAccountToken = import("./serviceAccountToken").ServiceAccountToken;
export const ServiceAccountToken: typeof import("./serviceAccountToken").ServiceAccountToken = null as any;
utilities.lazyLoad(exports, ["ServiceAccountToken"], () => require("./serviceAccountToken"));

export { ServiceTokenArgs, ServiceTokenState } from "./serviceToken";
export type ServiceToken = import("./serviceToken").ServiceToken;
export const ServiceToken: typeof import("./serviceToken").ServiceToken = null as any;
utilities.lazyLoad(exports, ["ServiceToken"], () => require("./serviceToken"));

export { WebhookArgs, WebhookState } from "./webhook";
export type Webhook = import("./webhook").Webhook;
export const Webhook: typeof import("./webhook").Webhook = null as any;
utilities.lazyLoad(exports, ["Webhook"], () => require("./webhook"));


// Export sub-modules:
import * as config from "./config";
import * as integration from "./integration";
import * as projectmember from "./projectmember";
import * as secretssync from "./secretssync";
import * as types from "./types";

export {
    config,
    integration,
    projectmember,
    secretssync,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "doppler:index/branchConfig:BranchConfig":
                return new BranchConfig(name, <any>undefined, { urn })
            case "doppler:index/environment:Environment":
                return new Environment(name, <any>undefined, { urn })
            case "doppler:index/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "doppler:index/groupMember:GroupMember":
                return new GroupMember(name, <any>undefined, { urn })
            case "doppler:index/project:Project":
                return new Project(name, <any>undefined, { urn })
            case "doppler:index/projectRole:ProjectRole":
                return new ProjectRole(name, <any>undefined, { urn })
            case "doppler:index/secret:Secret":
                return new Secret(name, <any>undefined, { urn })
            case "doppler:index/serviceAccount:ServiceAccount":
                return new ServiceAccount(name, <any>undefined, { urn })
            case "doppler:index/serviceAccountToken:ServiceAccountToken":
                return new ServiceAccountToken(name, <any>undefined, { urn })
            case "doppler:index/serviceToken:ServiceToken":
                return new ServiceToken(name, <any>undefined, { urn })
            case "doppler:index/webhook:Webhook":
                return new Webhook(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("doppler", "index/branchConfig", _module)
pulumi.runtime.registerResourceModule("doppler", "index/environment", _module)
pulumi.runtime.registerResourceModule("doppler", "index/group", _module)
pulumi.runtime.registerResourceModule("doppler", "index/groupMember", _module)
pulumi.runtime.registerResourceModule("doppler", "index/project", _module)
pulumi.runtime.registerResourceModule("doppler", "index/projectRole", _module)
pulumi.runtime.registerResourceModule("doppler", "index/secret", _module)
pulumi.runtime.registerResourceModule("doppler", "index/serviceAccount", _module)
pulumi.runtime.registerResourceModule("doppler", "index/serviceAccountToken", _module)
pulumi.runtime.registerResourceModule("doppler", "index/serviceToken", _module)
pulumi.runtime.registerResourceModule("doppler", "index/webhook", _module)
pulumi.runtime.registerResourcePackage("doppler", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:doppler") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
